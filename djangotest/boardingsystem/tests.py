from django.test import TestCase, Client
import json

# Create your tests here.
client = Client()


class BoardingPassTest(TestCase):
    def setUp(self):
        self.input_payload = [
            {"source": "Gerona Airport","destination": "Stockholm", "mode": "plane","journey_details": "Gate 45B, seat 3A.Baggage drop at ticket counter 344.","mode_details": "SK 455"},
            {"source": "Stockholm", "destination": "Newyork JFK", "mode": "plane", "journey_details": "Gate 22, Seat 7b", "mode_details": "SK22"},
            {"source": "Madrid","destination": "Barcelona", "mode": "train","journey_details": "Seat 45B","mode_details": "78A"},
            {"source": "Barcelona","destination": "Gerona Airport", "mode": "Airport Bus","journey_details": "","mode_details": ""},

        ]
        self.output_payload = [
            {"source": "Madrid", "destination": "Barcelona", "mode": "train", "journey_details": "Seat 45B", "mode_details": "78A"},
            {"source": "Barcelona", "destination": "Gerona Airport", "mode": "Airport Bus", "journey_details": "", "mode_details": ""},
            {"source": "Gerona Airport", "destination": "Stockholm", "mode": "plane","journey_details": "Gate 45B, seat 3A.Baggage drop at ticket counter 344.", "mode_details": "SK 455"},
            {"source": "Stockholm", "destination": "Newyork JFK", "mode": "plane", "journey_details": "Gate 22, Seat 7b", "mode_details": "SK22"}]
        self.empty_payload = []
        self.empty_payload_response_message = 'Input cannot be empty'

        self.invalid_payload = [
            # typo in source for first object
            {"sourc": "Madrid", "journey_details": "45B", "destination": "Barcelona", "mode": "train",
             "mode_details": "78A"},
            {"source": "Barcelona", "journey_details": "", "destination": "Gerona Airport", "mode": "Airport Bus",
             "mode_details": ""},
            {"source": "Gerona Airport", "journey_details": "Gate 45B, seat 3A.Baggage drop at ticket counter 344.",
             "destination": "Stockholm", "mode": "Airport Bus", "mode_details": "SK 455"},
            {"source": "Stockholm", "journey_details": "Gate 22, Seat 7b", "destination": "Newyork JFK",
             "mode": "plane", "mode_details": "SK22"}
        ]
        self.invalid_payload_response_message = 'Input data is invalid'

    def test_sort_unsorted_boarding_passes(self):
        response = client.post(
            '/boarding_system/boarding_pass/sort',
            data=json.dumps(self.input_payload),
            content_type='application/json'
        )
        self.assertEqual(response.data["data"], self.output_payload)

    def test_unchanged_sorted_boarding_passes(self):
        response = client.post(
            '/boarding_system/boarding_pass/sort',
            data=json.dumps(self.output_payload),
            content_type='application/json'
        )
        self.assertEqual(response.data["data"], self.output_payload)

    def test_with_empty_input(self):
        response = client.post(
            '/boarding_system/boarding_pass/sort',
            data=json.dumps(self.empty_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data["message"], self.empty_payload_response_message)

    def test_with_invalid_input(self):
        response = client.post(
            '/boarding_system/boarding_pass/sort',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data["message"], self.invalid_payload_response_message)
