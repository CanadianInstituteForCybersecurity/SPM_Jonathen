#!/usr/bin/env python3

def capitalize_names(names):
    return [name.title() for name in names]


def main():
    # Hardcoded list of names
    names = [
        "pedro cuvelier",
        "juan perez",
        "maria lopez",
        "carlos santana",
        "ana maria",
    ]

    print("Original Names:")
    for name in names:
        print(name)

    # Capitalize names
    capitalized = capitalize_names(names)

    print("\nCapitalized Names:")
    for name in capitalized:
        print(name)


if __name__ == "__main__":
    main()
