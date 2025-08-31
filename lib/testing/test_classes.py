#!/usr/bin/env python3
"""
Test script for Dog and Person classes
"""

from dog import Dog
from person import Person

def test_dog_class():
    print("=== Testing Dog Class ===")
    
    # Create a Dog instance
    fido = Dog()
    
    # Test bark method
    print("Testing bark():")
    fido.bark()  # Should print "Woof!"
    
    # Test sit method
    print("Testing sit():")
    fido.sit()   # Should print "The dog is sitting."
    
    print()

def test_person_class():
    print("=== Testing Person Class ===")
    
    # Create a Person instance
    person = Person()
    
    # Test talk method
    print("Testing talk():")
    person.talk()  # Should print "Hello World!"
    
    # Test walk method
    print("Testing walk():")
    person.walk()  # Should print "The person is walking."
    
    print()

def test_multiple_instances():
    print("=== Testing Multiple Instances ===")
    
    # Test multiple dogs
    dog1 = Dog()
    dog2 = Dog()
    
    print("Dog 1 barking:")
    dog1.bark()
    print("Dog 2 sitting:")
    dog2.sit()
    
    # Test multiple people
    person1 = Person()
    person2 = Person()
    
    print("Person 1 talking:")
    person1.talk()
    print("Person 2 walking:")
    person2.walk()

if __name__ == "__main__":
    test_dog_class()
    test_person_class()
    test_multiple_instances()