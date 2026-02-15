package compliance

violation[msg] {
  input.kind == "TraceEvent"

  required := {"lotCode", "sourceFacility", "destinationFacility", "timestamp"}
  provided := {k | input.spec[k]}
  missing := required - provided

  count(missing) > 0
  msg := sprintf("Missing required fields: %v", [missing])
}
