from hello import message


class TestMessage:
    def test_it_should_greet_the_world_on_no_arguments(self):
        empty_args_list = []

        result = message(empty_args_list)

        # in pytest the pattern is:
        # assert actual == expected
        assert result == "Hello World!"

    def test_it_should_greet_the_person_on_one_argument(self):
        args_with_a_name = ['Giangiorgio']

        result = message(args_with_a_name)

        assert result == "Hello Giangiorgio!"
