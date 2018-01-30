from django.shortcuts import render, redirect
from .models.db import models

class UserManager (models.Managr):
    def register (self, first, last, username , email, dob, password):
        response = {
            "valid": True,
            "errors":[],
            "user": None
        }

        if len (first)  < 1:
            response["errors"] .append ("First name is required")
        elif len(first) < 2:
            response["errors"] .append("First name must be 2 characters or longer")
        if len (last) < 1:
            response["errors"] .append("Last name is required")
        if len(last) < 2:
            response["errors"] .append("Last name must be 2 characters or longer")
        if len (username) <1:
            response["errors"] .append("Username name is required")
        if len (username) <3:
            response["errors"] .append("Username must be 3 character or longer")
        if len(email)

        elif not EMAIL

        if len(email)

        if len(email)








