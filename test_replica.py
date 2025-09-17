#!/usr/bin/env python3
"""Test the DeepBlue replica system."""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from deepblue_replica_system import deepblue_replica
    print("✅ DeepBlue replica system imported successfully")
    
    # Test initialization
    result = deepblue_replica.initialize_system()
    print(f"✅ Initialization: {result['success']}")
    
    # Test query
    query_result = deepblue_replica.query_system(
        "Test query",
        "i think we need a bigger boat"
    )
    print(f"✅ Query test: {query_result['success']}")
    
    print("🎉 All tests passed!")
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    sys.exit(1)
