import asyncio
from playwright.async_api import async_playwright

async def login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            # Navigate to the login page
            await page.goto("http://the-internet.herokuapp.com/login")

            # Wait until the page is fully loaded
            await page.wait_for_load_state('load')

            # Confirm navigation status
            if page.url == "http://the-internet.herokuapp.com/login":
                print("Navigation to login page successful")
            else:
                print("Navigation to login page failed")

            # Fill in the username and password fields
            await page.fill('input[name="username"]', 'tomsmith')
            await page.fill('input[name="password"]', 'SuperSecretPassword!')

            # Click the login button
            await page.click('button[type="submit"]')

            # Wait for navigation to complete
            await page.wait_for_load_state('load')

            # Check if login was successful
            if await page.is_visible('text="Logout"'):
                print("Login successful!")
            else:
                print("Login failed.")

        except Exception as e:
            print(f"Error during login: {e}")

        finally:
            # await asyncio.sleep(30)
            await browser.close()

# Run the login function asynchronously
asyncio.run(login())
