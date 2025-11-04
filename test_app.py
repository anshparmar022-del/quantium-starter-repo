import pytest
from dash.testing.application_runners import import_app

# Import the Dash app
@pytest.fixture
def app_runner(dash_duo):
    # Import your app.py (no .py extension needed)
    app = import_app("app")
    dash_duo.start_server(app)
    return dash_duo

# ----------------------------
# 1️⃣ Test Header Presence
# ----------------------------
def test_header_is_present(app_runner):
    app_runner.wait_for_text_to_equal("h1", "Soul Foods - Pink Morsel Sales Visualizer")
    assert app_runner.find_element("h1").text == "Soul Foods - Pink Morsel Sales Visualizer"

# ----------------------------
# 2️⃣ Test Graph Presence
# ----------------------------
def test_graph_is_present(app_runner):
    graph = app_runner.find_element("#sales-line-chart")
    assert graph is not None
    assert graph.tag_name == "div" or graph.tag_name == "svg"  # depending on rendering

# ----------------------------
# 3️⃣ Test Region Filter Presence
# ----------------------------
def test_region_filter_is_present(app_runner):
    radio_group = app_runner.find_element("#region-filter")
    assert radio_group is not None
