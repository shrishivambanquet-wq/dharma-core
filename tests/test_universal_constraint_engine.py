from engine.universal_constraint_engine import UniversalConstraintEngine

def test_engine_allows_placeholder_action():
    engine = UniversalConstraintEngine()
    result = engine.evaluate("demo_action", {})
    assert result["allowed"] is True
    assert "reason" in result
