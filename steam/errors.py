# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2020 James

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import re


class SteamException(Exception):
    """Base exception class for steam.py"""
    pass


class ClientException(SteamException):
    """Exception that's thrown when something isn't possible
    but is handled by the client.
    Subclass of :exc:`SteamException`
    """


class HTTPException(SteamException):  # TODO add some messages for these
    """Exception that's thrown for any web API error.
    Subclass of :exc:`SteamException`
    """

    def __init__(self, response, data):
        self.response = response
        self.status = response.status

        if isinstance(data, dict):
            message = list(data.values())[0]
            code_regex = re.compile(r'[^\s]([0-9]{1,3})[^\s]')
            code = re.findall(code_regex, message)[0]
            if code:
                self.code = int(code)  # would like to EResult however steam trades don't use the same system
                self.message = re.sub(code_regex, '', message).replace('  ', ' ')
            else:
                self.code = 0
                self.message = message
        else:
            self.message = data
            self.code = 0
        super().__init__(f'{response.status} {response.reason} (error code: {self.code})'
                         f'{f": {self.message}" if self.message else ""}')


class Forbidden(HTTPException):
    """Exception that's thrown when status code 403 occurs.
    Subclass of :exc:`HTTPException`
    """
    pass


class NotFound(HTTPException):
    """Exception that's thrown when status code 404 occurs.
    Subclass of :exc:`HTTPException`
    """
    pass


class LoginError(SteamException):
    """Exception that's thrown when a login fails.
    Subclass of :exc:`SteamException`
    """
    pass


class InvalidCredentials(LoginError):
    """Exception that's thrown when credentials are incorrect.
    Subclass of :exc:`LoginError`
    """
    pass


class SteamAuthenticatorError(LoginError):
    """Exception that's thrown when steam cannot authenticate your details.
    Subclass of :exc:`LoginError`
    """
    pass


class ConfirmationError(SteamAuthenticatorError):
    """Exception that's thrown when a confirmation fails.
    Subclass of :exc:`SteamAuthenticatorError`
    """
    pass
