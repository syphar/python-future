from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future.builtins import super
from future import standard_library
import io
import unittest
with standard_library.hooks():
    import email
    from email.message import Message
    from future.tests.test_email import TestEmailBase


class TestCustomMessage(TestEmailBase):

    class MyMessage(Message):
        def __init__(self, policy):
            self.check_policy = policy
            super().__init__()

    MyPolicy = TestEmailBase.policy.clone(linesep='boo')

    def test_custom_message_gets_policy_if_possible_from_string(self):
        msg = email.message_from_string("Subject: bogus\n\nmsg\n",
                                        self.MyMessage,
                                        policy=self.MyPolicy)
        self.assertTrue(isinstance(msg, self.MyMessage))
        self.assertIs(msg.check_policy, self.MyPolicy)

    def test_custom_message_gets_policy_if_possible_from_file(self):
        source_file = io.StringIO("Subject: bogus\n\nmsg\n")
        msg = email.message_from_file(source_file,
                                      self.MyMessage,
                                      policy=self.MyPolicy)
        self.assertTrue(isinstance(msg, self.MyMessage))
        self.assertIs(msg.check_policy, self.MyPolicy)

    # XXX add tests for other functions that take Message arg.


if __name__ == '__main__':
    unittest.main()
