from utils.driver import WebDriver
from utils.gmail_utils import send_email
import pytest


class TestClass:
    @pytest.fixture()
    def test_setup(self):
        self.driver = WebDriver()
        # yield
        # self.driver.quit()

    def test_nada_email(self, test_setup):
        self.driver.go_to_url('https://getnada.com')
        nada_email = self.driver.copy_new_email()
        assert '@getnada.com' in nada_email

    def test_random_urls(self, test_setup):
        urls = ['https://aws.random.cat/meow', 'https://random.dog/woof.json', 'https://randomfox.ca/floof/']
        l1 = [self.driver.copy_picture(i) for i in urls]
        assert len(l1) == 3
        for item in l1:
            assert isinstance(item, dict)

    def test_send_email_to_getnada_with_pictures(self, test_setup):
        self.driver.go_to_url('https://getnada.com')
        nada_email = self.driver.copy_new_email()
        urls = ['https://aws.random.cat/meow', 'https://random.dog/woof.json', 'https://randomfox.ca/floof/']
        l1 = [self.driver.copy_picture(i) for i in urls]
        send_email(nada_email, l1, 'testslugovoi@gmail.com')
        self.driver.go_to_url('https://getnada.com')
        l2 = self.driver.chek_received_email()
        assert str(l1) == l2, f'Expected message: {l1}. Actual message: {l2}'

