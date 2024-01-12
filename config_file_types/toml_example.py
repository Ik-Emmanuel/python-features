import tomllib


def main() -> None:
    with open("setting.toml", "rb") as f:
        data = tomllib.load(f)
        print(data)


if __name__ == "__main__":
    main()