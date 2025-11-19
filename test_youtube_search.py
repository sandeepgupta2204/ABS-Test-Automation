from playwright.sync_api import sync_playwright

def test_youtube_search():
    with sync_playwright() as p:
        # Launch actual installed Google Chrome in non-headless mode
        context = p.chromium.launch_persistent_context(
            user_data_dir="/tmp/playwright",  # temporary profile
            headless=False,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            slow_mo=500
        )
        page = context.new_page()

        # Step 1: Open YouTube
        page.goto("https://www.youtube.com")

        # Step 2: Search for a video
        page.fill("input#search", "Selenium Python tutorial")

        # Step 3: Click the search button
        page.click("button#search-icon-legacy")

        # Step 4: Wait for results to appear
        page.wait_for_selector("ytd-video-renderer", timeout=10000)

        # Step 5: Validate that results are present
        video_titles = page.query_selector_all("ytd-video-renderer")
        assert len(video_titles) > 0, "❌ No search results found on YouTube!"

        print(f"✅ Test passed! Found {len(video_titles)} video results for 'Selenium Python tutorial'.")

        # Step 6: Wait a bit before closing
        page.wait_for_timeout(5000)
        context.close()
