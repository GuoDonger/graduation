from django.forms import fields,  Form
from captcha.fields import CaptchaField


class UserRegisterForm(Form):
    email = fields.CharField(
        required=True,
        error_messages={'required': '邮箱必须填写'}
    )
    password = fields.CharField(
        min_length=6,
        max_length=12,
        required=True,
        error_messages={'required': '密码必须填写', 'min_length': '密码最少6位', 'max_length': '密码最长12位'}
    )
    captcha = CaptchaField(
        error_messages={'invalid': '验证码错误'}
    )


class UserLoginForm(Form):
    email = fields.CharField(
        required=True,
        error_messages={'required': '用户名必须填写'}
    )
    password = fields.CharField(
        min_length=6,
        max_length=12,
        required=True,
        error_messages={'required': '密码必须填写', 'min_length': '密码最少6位', 'max_length': '密码最长12位'}
    )


class UserForgetForm(Form):
    email = fields.CharField(
        required=True,
        error_messages={'required': '用户名必须填写'}
    )
    captcha = CaptchaField(
        error_messages={'invalid': '验证码错误'}
    )




