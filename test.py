import ast
import importlib
import itertools
import os

import astor
import black
import isort
import reflect as r


def format(code):
    try:
        return isort.code(black.format_str(code, mode=black.FileMode()))
    except Exception as e:
        raise
        print(e)
        return code


class RemoveImportFrom(ast.NodeTransformer):
    def __init__(self, names={}):
        self.names = names

    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.level > 0 or any(
            node.module.startswith(name) for name in ["demos", "website"]
        ):
            return node
        qualified_name = module_name = node.module
        if module_name.startswith("reflect") and not module_name in [
            "reflect_utils",
            "reflect_bokeh",
        ]:
            module_name_split = module_name.split("_", 1)
            qualified_name = asname = (
                module_name_split[1] if len(module_name_split) == 2 else "r"
            )
        else:
            asname, module_name = None, module_name.split(".", 1)[0]
        for alias in node.names:
            alias_name = alias.name
            if alias_name != "*":
                self.names[alias.asname or alias_name] = qualified_name, alias_name
        return ast.Import(
            names=[ast.alias(name=module_name, asname=asname)], ctx=ast.Load()
        )

    def visit_Name(self, node: ast.Name):
        match = self.names.get(node.id)
        if match:
            if isinstance(match, tuple):
                module, name = match
                return ast.Attribute(value=ast.Name(id=module), attr=name)
        return node


def list_all_files(folder, filter=None):
    return itertools.chain.from_iterable(
        (
            os.path.join(root, name)
            for name in files
            if not filter or filter(os.path.join(root, name))
        )
        for root, _dirs, files in os.walk(folder)
    )


def refactor_module(source: str, names) -> str:
    return format(astor.to_source(RemoveImportFrom(names).visit(ast.parse(source))))


def main():
    nb_examples_valid, nb_examples = 0, 0
    python_modules = list_all_files(
        "snippets",
        filter=lambda path: path.endswith(".py")
        and not any(n in path for n in ["invalid", "packages", "matplotlib_examples"]),
    )
    # python_modules = (
    #     path
    #     for path in os.listdir(".")
    #     if path.endswith(".py") and not path in ["home.py", "folder_hierarchy.py"]
    # )
    m = importlib.import_module("test_refactor")
    temp_module_counter = itertools.count()
    for path in python_modules:
        print(path)
        nb_examples += 1
        new_content = refactor_module(open(path).read(), {})
        open(path, "w").write(new_content)
        continue
        try:
            m = importlib.import_module(path[0:-3].replace("/", "."))
        except Exception as e:
            continue
        if not hasattr(m, "app"):
            continue
        try:
            c = m.app()
        except Exception as e:
            continue
        assert isinstance(c, r.Component)
        nb_examples_valid += 1
        names = {}
        while True:
            temp_module_name = f"test_refactor_{next(temp_module_counter)}"
            new_content = refactor_module(open(path).read(), names)
            try:
                open(temp_module_name + ".py", "w").write(new_content)
                importlib.import_module(temp_module_name).app()
                open(path, "w").write(new_content)
                break
            except NameError as e:
                name = e.args[0].split(" ")[1][1:-1]
                names[name] = "html", name
            finally:
                os.remove(temp_module_name + ".py")
    print(nb_examples, nb_examples_valid)
    print("-" * 30)


if __name__ == "__main__":
    main()
