import pytest
import allure
from playwright.sync_api import sync_playwright, Page,expect
import time


@pytest.fixture(scope="function")
def setup_teardown():
    """Fixture to initialize and teardown Playwright browser and page."""
    playwright = sync_playwright().start()  # Start Playwright
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Load the login page
    page.goto("https://katalon-demo-cura.herokuapp.com/")
    page.wait_for_load_state("networkidle")
    time.sleep(3)  # Reduce unnecessary sleep time
    yield page  # Provide the page object to tests

    # Teardown
    context.close()
    browser.close()
    playwright.stop()  # Ensure Playwright is properly stopped

@pytest.mark.positive
def test_miniproject2(setup_teardown):
    """
    this is working with selected date
    :param setup_teardown:
    :return:
    """
    page = setup_teardown

    expect(page).to_have_title("CURA Healthcare Service")
    page.locator("#btn-make-appointment").click()
    expect(page).to_have_url("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    page.locator("#txt-username").click()
    page.locator("#txt-username").fill("John Doe")
    time.sleep(1)
    page.locator("//input[@id='txt-password']").click()
    page.locator("//input[@id='txt-password']").fill("ThisIsNotAPassword")
    time.sleep(1)
    page.locator("//button[@id='btn-login']").click()
    page.wait_for_load_state("networkidle")
    time.sleep(3)
    expect(page).to_have_url("https://katalon-demo-cura.herokuapp.com/#appointment")
    #to select select option to place of hospital
    try:
        page.get_by_label("Facility").select_option("Hongkong CURA Healthcare Center")
        print("\n get_by_label selection")
    except:
        page.locator("#combo_facility").select_option("Hongkong CURA Healthcare Center")
        print("\n selection by css selector")

        # Optionally, verify the selection
        selected_value = page.locator("#combo_facility").input_value()
        print(f"Selected value_XXX: {selected_value}")
    page.get_by_label('Medicaid').check()  # to select radio button)

    #date input
    time.sleep(2)
    page.get_by_placeholder("dd/mm/yyyy").click()
    time.sleep(3)
    page.get_by_role("cell", name="18").click()
    page.get_by_placeholder("dd/mm/yyyy").press("Tab")
    time.sleep(3)

    try:
        page.get_by_label("Comment").focus()
        time.sleep(3)
        page.get_by_label("Comment").fill("I have fever since yesterday!")
        print("\ncomment filled by get_by_label")
    except:
        page.locator("#txt_comment").fill("I have fever issue!")
        print("\ncomment filled by css selector")
    time.sleep(3)

    page.locator("//button[@id='btn-book-appointment']").click()
    time.sleep(3)

    result = page.locator("//h2[normalize-space()='Appointment Confirmation']").text_content()
    assert result == "Appointment Confirmation"

    time.sleep(2)

@pytest.mark.positive
def test_trial(setup_teardown):
    """
    This is working smoothly with date selection but not 100%
    :param setup_teardown:
    :return:
    """

    page = setup_teardown

    page.get_by_role("link", name="Make Appointment").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("John Doe")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("ThisIsNotAPassword")
    page.get_by_role("button", name="Login").click()
    page.get_by_label("Facility").select_option("Hongkong CURA Healthcare Center")
    page.get_by_label("Medicaid").check()
    time.sleep(1)
    page.get_by_placeholder("dd/mm/yyyy").click()
    page.get_by_role("cell", name="«").click()
    #page.get_by_role("cell", name="12").click()
    time.sleep(1)
    page.get_by_role("cell", name="21").click()
    page.get_by_placeholder("dd/mm/yyyy").click()
    time.sleep(1)
    page.get_by_placeholder("dd/mm/yyyy").press("Tab")
    time.sleep(1)
    page.get_by_placeholder("Comment").fill("I have fever!")
    time.sleep(1)
    page.get_by_role("button", name="Book Appointment").click()
    page.get_by_role("heading", name="Appointment Confirmation").click()
    time.sleep(6)

@pytest.mark.positive
def test_trial2(setup_teardown):
    """
    This is working with previous selected date
    :param setup_teardown:
    :return:
    """
    page = setup_teardown

    page.get_by_role("link", name="Make Appointment").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("John Doe")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("ThisIsNotAPassword")
    page.get_by_role("button", name="Login").click()
    page.get_by_label("Facility").select_option("Hongkong CURA Healthcare Center")
    page.get_by_label("Medicaid").check()
    time.sleep(1)

    page.get_by_placeholder("dd/mm/yyyy").click()
    page.get_by_role("cell", name="«").click()
    #page.get_by_role("cell", name="12").click()
    time.sleep(1)
    page.get_by_role("cell", name="21").click()
    page.get_by_placeholder("dd/mm/yyyy").click()
    time.sleep(1)
    page.get_by_placeholder("dd/mm/yyyy").press("Tab")
    time.sleep(1)

    page.get_by_placeholder("Comment").fill("I have fever!")
    time.sleep(1)
    page.get_by_role("button", name="Book Appointment").click()
    page.get_by_role("heading", name="Appointment Confirmation").click()
    time.sleep(6)



@pytest.mark.positive
def test_trial3(setup_teardown):
    """
    this is working for the future date
    :param setup_teardown:
    :return:
    """
    page = setup_teardown

    page.get_by_role("link", name="Make Appointment").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("John Doe")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("ThisIsNotAPassword")
    page.get_by_role("button", name="Login").click()
    page.get_by_label("Facility").select_option("Hongkong CURA Healthcare Center")
    page.get_by_label("Medicaid").check()
    time.sleep(1)


    page.get_by_placeholder("dd/mm/yyyy").click()
    time.sleep(3)
    page.get_by_role("cell", name="»").click()
    time.sleep(1)
    """
    page.get_by_role("cell", name="»").click()
    time.sleep(1)
    page.get_by_role("cell", name="»").click()
    time.sleep(1)
    page.get_by_role("cell", name="»").click()
    time.sleep(1)
    """
    page.get_by_role("cell", name="15").click()
    page.get_by_placeholder("dd/mm/yyyy").press("Tab")
    time.sleep(3)
    page.get_by_placeholder("Comment").fill("I have fever!")
    time.sleep(1)
    page.get_by_role("button", name="Book Appointment").click()
    page.get_by_role("heading", name="Appointment Confirmation").click()
    time.sleep(6)


@pytest.mark.positive
def test_trial4(setup_teardown):
    """
    this is working for the current date
    :param setup_teardown:
    :return:
    """
    page = setup_teardown

    page.get_by_role("link", name="Make Appointment").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("John Doe")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("ThisIsNotAPassword")
    page.get_by_role("button", name="Login").click()
    page.get_by_label("Facility").select_option("Hongkong CURA Healthcare Center")
    page.get_by_label("Medicaid").check()
    time.sleep(1)


    page.get_by_placeholder("dd/mm/yyyy").click()
    time.sleep(3)
    page.get_by_role("cell", name="18").click()
    page.get_by_placeholder("dd/mm/yyyy").press("Tab")
    time.sleep(3)
    page.get_by_placeholder("Comment").fill("I have fever!")
    time.sleep(1)
    page.get_by_role("button", name="Book Appointment").click()
    page.get_by_role("heading", name="Appointment Confirmation").click()
    time.sleep(6)

@pytest.mark.positive
def test_trial5(setup_teardown):
    """
    this is working for the previous date
    :param setup_teardown:
    :return:
    """
    page = setup_teardown

    page.get_by_role("link", name="Make Appointment").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("John Doe")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("ThisIsNotAPassword")
    page.get_by_role("button", name="Login").click()
    page.get_by_label("Facility").select_option("Hongkong CURA Healthcare Center")
    page.get_by_label("Medicaid").check()
    time.sleep(2)

    page.get_by_placeholder("dd/mm/yyyy").click()
    page.get_by_role("cell", name="«").click()
    # page.get_by_role("cell", name="12").click()
    time.sleep(2)
    page.get_by_role("cell", name="11").click()
    #page.get_by_placeholder("dd/mm/yyyy").click()
    time.sleep(1)
    page.get_by_placeholder("dd/mm/yyyy").press("Tab")
    time.sleep(1)


    """
    page.get_by_role("cell", name="»").click()
    time.sleep(1)
    page.get_by_role("cell", name="»").click()
    time.sleep(1)
    page.get_by_role("cell", name="»").click()
    time.sleep(1)
    page.get_by_role("cell", name="»").click()
    time.sleep(1)
    """

    page.get_by_placeholder("Comment").fill("I have fever!")
    time.sleep(1)
    page.get_by_role("button", name="Book Appointment").click()
    page.get_by_role("heading", name="Appointment Confirmation").click()
    time.sleep(6)