import json,math,sys,unittest
from copy import deepcopy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools"))
from planning import capacity,staffing
ROOT=Path(__file__).resolve().parents[1]
class PlanningTests(unittest.TestCase):
 def setUp(self):self.data=json.loads((ROOT/"examples/planning/capacity.json").read_text());self.people=json.loads((ROOT/"examples/planning/staffing.json").read_text())
 def test_decimal_ingest_and_nonoverlapping_tiers(self):
  result=capacity(self.data);self.assertEqual(result["raw_gb_per_day"],86.4);self.assertAlmostEqual(result["hot_gb"],2358.72);self.assertAlmostEqual(result["additional_cold_gb"],10130.4)
 def test_outage_and_net_drain(self):
  result=capacity(self.data);self.assertEqual(result["backlog_events"],72000000);self.assertEqual(result["raw_queue_gb"],72);self.assertEqual(result["catchup_hours"],10)
 def test_no_headroom_does_not_produce_fake_zero_recovery(self):
  self.data["processing_eps"]=1000;result=capacity(self.data);self.assertIsNone(result["catchup_hours"]);self.assertFalse(result["finite_catchup_possible"])
 def test_overloaded_consumer_cannot_clear_backlog(self):
  self.data["processing_eps"]=900;self.assertIsNone(capacity(self.data)["catchup_hours"])
 def test_zero_backlog_with_zero_margin_still_marks_no_headroom(self):
  self.data.update(outage_hours=0,processing_eps=1000);result=capacity(self.data);self.assertEqual(result["catchup_hours"],0);self.assertFalse(result["recovery_headroom_available"])
 def test_peak_cannot_be_less_than_average(self):
  self.data["peak_eps"]=999
  with self.assertRaises(ValueError):capacity(self.data)
 def test_nonfinite_and_boolean_inputs_rejected(self):
  for value in (float("nan"),float("inf"),True):
   with self.subTest(value=value):
    d=deepcopy(self.data);d["event_bytes"]=value
    with self.assertRaises(ValueError):capacity(d)
 def test_negative_outage_rejected(self):
  self.data["outage_hours"]=-1
  with self.assertRaises(ValueError):capacity(self.data)
 def test_compression_and_integer_copies_bounded(self):
  for key,value in (("stored_to_raw_ratio",1.1),("hot_copies",1.5),("cold_copies",0)):
   with self.subTest(key=key):
    d=deepcopy(self.data);d[key]=value
    with self.assertRaises(ValueError):capacity(d)
 def test_mean_staffing_uses_max_not_sum(self):
  r=staffing(self.people);self.assertEqual(r["coverage_fte"],10.5);self.assertAlmostEqual(r["workload_fte"],140/15.68);self.assertEqual(r["planning_fte_lower_bound"],10.5);self.assertEqual(r["rounded_planning_fte"],11)
 def test_workload_can_exceed_rota_lower_bound(self):
  self.people["alerts_per_day"]=600;r=staffing(self.people);self.assertGreater(r["workload_fte"],r["coverage_fte"]);self.assertEqual(r["planning_fte_lower_bound"],r["workload_fte"])
 def test_invalid_staffing_ratios_rejected(self):
  for key,value in (("target_utilization",1),("availability_ratio",0),("productive_ratio",1.2)):
   with self.subTest(key=key):
    d=deepcopy(self.people);d[key]=value
    with self.assertRaises(ValueError):staffing(d)
if __name__=="__main__":unittest.main()
