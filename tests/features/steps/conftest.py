import pytest
from pytest_bdd import given
from selenium import webdriver


# Constants

GAM_BO = 'https://gam-gam-renovacion-backoffice.development.mag.dev'

# Hooks


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')

# Fixtures

