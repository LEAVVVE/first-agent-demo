"""最小命令行聊天助手。"""


def generate_reply(user_message: str) -> str:
    """根据用户输入生成最简单的回复。"""
    return f"你说的是：{user_message}"


def main() -> None:
    """启动命令行聊天循环。"""
    print("欢迎使用最小命令行聊天助手！")
    print("输入内容开始聊天，输入 exit / quit / q 退出。")

    while True:
        user_input = input("你: ").strip()

        if user_input.lower() in {"exit", "quit", "q"}:
            print("助手: 再见！")
            break

        if not user_input:
            print("助手: 你还没有输入内容。")
            continue

        reply = generate_reply(user_input)
        print(f"助手: {reply}")


if __name__ == "__main__":
    main()
