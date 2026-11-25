from datetime import datetime, timezone


class Telemetry:

    def __init__(self):
        self.events = []

    def record_event(self, event_type: str, product_id: str, details: str):
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event_type": event_type,
            "product_id": product_id,
            "details": details
        }

        self.events.append(event)

        return event

    def get_events(self):
        return self.events


telemetry = Telemetry()