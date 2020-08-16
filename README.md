README
======

Quick notes
-----------

Run all tests from root: `pytest`

Run all tests verbose: `pytest -v`

Show all print statements/info `pytest -s`

Run only one decorator: `pytest -m <name>`

Run tests that **must have** these decorators: `pytest -m "<name> and <name>"`

Run tests that **have any** of these decorators: `pytest -m "<name> or <name>"`

Run all tests **except** these decorators: `pytest -m "not <name> {and not <name>}"`

Decorators
----------

Markers must be defined in `pytest.ini`.

    [pytest]
    ...
    markers =
        marker1
        marker2

Markers should be documented in the `pytest.ini` file if they're supposed to be used. Ones to help you when writing the tests do not document. Developers/testers will look here for tests to run, it should be documented and clear.

Adding decorators:

    from pytest import mark

    @mark.<name>
    def test_my_test():
      ...

Decorators on a class, all methods get that marker:

    from pytest import mark

    @mark.<name1>
    class MyTests:
      def test_thing_as_expected(self):
        assert True
      
      @mark.<name2>
      def test_another_as_expected(self):
        assert True

Running `pytest -m name1`, everything gets executed thats in the class.

Running `pytest -m name2`, only name2 gets executed.

pytest.ini
----------

Not required, defaults used when `pytest` is run on its own.

File syntax and examples:

    [pytest]
    python_files = test_*
    python_classes = *Tests
    python_functions = test_*

    markers =
          body: Body test (optional messages)
          engine: Engine tests
          entertainment: Entertainment tests
          smoke

Execute `pytest --markers` will reveal optional messages for markers.

    (pytest_virtual) Joshuas-iMac:pytest joshua$ pytest --markers
    @pytest.mark.body: Body test

    @pytest.mark.engine: Engine tests

    @pytest.mark.entertainment: Entertainment tests

    @pytest.mark.smoke:
    ...

Fixtures
--------

Saves repeating importing and creating resources for multiple tests defined using **scope**.

    from pytest import fixture
    from selenium import webdriver

    @fixture(scope='function')
    def chrome_browser():
      browser = webdriver.Chrome()
      return browser
    
Test function consumes the fixture:

    @mark.ui
    def test_navigate_to_this_page(chrome_browser):
      chrome_browser.get('https://example.com')
      assert True

Scopes:

- session = exist until all tests are run
- function = exist only for duration of test

Advanced
- - - -

Yield a fixture contents to use the same browser:

    @fixture(scope='session')
    def chrome_browser():
      browser = webdriver.Chrome()
      yield browser

pytest-html
-----------

`pip install pytest-html`

`pytest --html="results.html"`

Jenkins XML
-----------

`pytest --juinit-xml="results.xml"`

Under Build, execute shell:

Command: `cd tests && pytest --junit-xml="BUILD_${BUILD_NUMBER}_results.xml"`

Add `Publish JUnit test result report`.

Test report XMLs: `/tests/*.xml`