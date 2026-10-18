import allure
from pages.widgets.tool_tips_page import ToolTipsPage

@allure.epic("demoqa_tests")
@allure.feature("widgets")
@allure.story("checking tool tips")
@allure.severity(allure.severity_level.NORMAL)
def test_tool_tips_hover(test_tool_tips):
    tool_tips = ToolTipsPage(test_tool_tips)
    tool_tips.hover_button_and_check_tooltip()
    tool_tips.hover_text_field_and_check_tooltip()
    tool_tips.hover_text_field_and_check_tooltip()

