import asyncio
from app import ExpenseApp


async def main():
    app = ExpenseApp()
    await app.run()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nChương trình đã dừng theo yêu cầu người dùng.')
