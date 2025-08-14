from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Todo

# Create your tests here.
class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="Homework part1",
            body="Read book till chapter5"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Homework part1")
        self.assertEqual(self.todo.body, "Read book till chapter5")
        self.assertEqual(str(self.todo), "Homework part1")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "Homework part1")