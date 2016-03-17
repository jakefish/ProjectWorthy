
class AbstractUser(object):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """
    String username = ""

    String first_name = ""
    String last_name = ""
    String email = ""
    bool is_staff = False
    bool is_active = False
    int date_joined = 0

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return full_name

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, **kwargs):
        """
        Sends an email to this User.
        """

class User(AbstractUser):

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
