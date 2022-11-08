from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath
    // *[ @ id = "login"]
    // *[contains(text(), ‘Login’ )]
    // child::div / a
    password_field_xpath
    // *[ @ id ="password"]
    // *[contains(text(), ‘Password’ )]
    // child::div / a
    sign_in_bottom_xpath
    // *[ @ id = "__next"] / form / div / div[2] / button / span[1]
    // *[text() =«S»ibn in]
    // child::div / a
    email = "pati.it.qa@gmail.com"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
