import json,sys,unittest
from copy import deepcopy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools"))
from design_review import review
ROOT=Path(__file__).resolve().parents[1]
class DesignReviewTests(unittest.TestCase):
 def setUp(self):self.data=json.loads((ROOT/"examples/designs/connected-enterprise.json").read_text())
 def codes(self,d):return {i["code"] for i in review(d)["issues"]}
 def test_reference_records_are_documentation_only(self):
  for name in ("connected-enterprise","disconnected-site"):
   r=review(json.loads((ROOT/f"examples/designs/{name}.json").read_text()));self.assertEqual(r["status"],"documentation_valid");self.assertIn("not authenticated",r["scope"])
 def test_disconnected_external_dependency_detected(self):
  d=json.loads((ROOT/"examples/designs/contradictory-disconnected.json").read_text());self.assertIn("external_offline_dependency",self.codes(d))
 def test_untrusted_proposal_cannot_be_declared_authority(self):
  self.data["response"]["independent_authorization"]=False;self.assertIn("proposal_as_authority",self.codes(self.data))
 def test_high_impact_actions_need_exact_approval_and_budget(self):
  self.data["response"].update(exact_expiring_approval=False,max_actions_per_job=0);self.assertTrue({"unbounded_approval","missing_action_budget"}<=self.codes(self.data))
 def test_stale_or_unverified_is_not_current(self):
  self.data["visibility"].update(reported_age_seconds=999,origin_verified=False);self.assertTrue({"stale_as_current","unverified_as_current"}<=self.codes(self.data))
 def test_tenant_boundary_and_owner_gaps_exposed(self):
  d=json.loads((ROOT/"examples/designs/incomplete-mssp.json").read_text());self.assertTrue({"missing_tenant_boundary","missing_owner"}<=self.codes(d))
 def test_declaration_does_not_support_environment_claim(self):
  self.data.update(sovereignty_claim="proven",evidence_claim="tested_environment");self.assertTrue({"declaration_as_assurance","unsupported_environment_claim"}<=self.codes(self.data))
 def test_fail_open_action_handling_rejected(self):
  self.data["response"]["failure_behavior"]="allow";self.assertIn("fail_open_response",self.codes(self.data))
 def test_malformed_freshness_is_not_healthy(self):
  self.data["visibility"]["reported_age_seconds"]=float("nan");self.assertIn("invalid_freshness",self.codes(self.data))
 def test_unknown_architecture_not_silently_accepted(self):
  self.data["pattern_id"]="P99";self.assertIn("unknown_pattern",self.codes(self.data))
 def test_nonobject_record_is_not_accepted_or_crashed(self):
  self.assertIn("invalid_record_shape",self.codes([]))
 def test_malformed_nested_records_are_not_healthy(self):
  self.data["response"]=[];self.assertIn("invalid_record_shape",self.codes(self.data))
if __name__=="__main__":unittest.main()
