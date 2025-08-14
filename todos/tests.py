from django.test import TestCase

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