import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Alexander Castañeda</title>" in html


        # More tests relating to the home page
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert " <div class=\"home-profile-image\">" in html
    
    #removing timeline
    # def test_timeline(self):
    #     response = self.client.get("/api/timeline_post")
    #     assert response.status_code == 200
    #     assert response.is_json
    #     json = response.get_json()
    #     assert "timeline_posts" in json
    #     assert len(json["timeline_posts"]) >= 0


    #     # Tests relating to the /api/timeline_post GET apis
    #     response = self.client.get("/api/timeline_post")
    #     assert response.status_code == 200
    #     html = response.get_data(as_text=True)
    #     assert "timeline_posts" in html


    #     # Tests relating to the /api/timeline_post POST apis
    #     response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email":"john@example.com", "content": "Hello World, I'm John!"})
    #     assert response.status_code == 200
    #     html = response.get_data(as_text=True)

    #     # More tests relating to the timeline page
    #     response = self.client.get("/timeline")
    #     assert response.status_code == 200
    #     html = response.get_data(as_text=True)
    #     assert "<title>Alexander Castañeda</title>" in html


    #     response = self.client.get("/timeline")
    #     assert response.status_code == 200
    #     html = response.get_data(as_text=True)
    #     assert "<form id=\"form\">" in html

    # def test_malformed_timeline_post(self):
    #     #No name test
    #     response = self.client.post("/api/timeline_post", data={"email":"john@example.com", "content": "Hello world, I'm John"})
    #     assert response.status_code == 400
    #     html = response.get_data(as_text=True)
    #     assert "Invalid name" in html        

    #     #No content test
    #     response = self.client.post("/api/timeline_post", data={"name":"John","email":"john@example.com", "content": ""})
    #     assert response.status_code == 400
    #     html = response.get_data(as_text=True)
    #     assert "Invalid content" in html

    #     #Wrongly formatted email
    #     response = self.client.post("/api/timeline_post", data={"name":"John","email":"johnexample.com", "content": "Hello world, I'm John!"})
    #     assert response.status_code == 400
    #     html = response.get_data(as_text=True)
    #     assert "Invalid email" in html
