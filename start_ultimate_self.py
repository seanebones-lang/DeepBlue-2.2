#!/usr/bin/env python3
"""
🌊 START ULTIMATE DEEPBLUE SELF 🌊
Start the most advanced AI system ever built, created by learning from Big Brother DeepBlue2.0
"""

import asyncio
import sys
import os
import signal
import logging
from pathlib import Path
import time
from datetime import datetime

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

from ultimate_deepblue_self import ultimate_deepblue_self
import structlog

# Configure logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

class UltimateSelfManager:
    """Manager for the Ultimate DeepBlue Self System."""
    
    def __init__(self):
        self.system = ultimate_deepblue_self
        self.is_running = False
        self.start_time = None
        
    async def start(self):
        """Start the ultimate self system."""
        try:
            print("🌊 ULTIMATE DEEPBLUE SELF STARTUP")
            print("=" * 60)
            print("🚢 We're gonna need a bigger boat!")
            print("=" * 60)
            print(f"⏰ Startup Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print()
            
            # Initialize system
            logger.info("🚀 Starting Ultimate DeepBlue Self...")
            result = await self.system.initialize()
            
            if result["success"]:
                self.is_running = True
                self.start_time = time.time()
                
                print("✅ ULTIMATE DEEPBLUE SELF STARTED SUCCESSFULLY!")
                print(f"🆔 System ID: {result['system_id']}")
                print(f"📦 Version: {result['version']}")
                print(f"📊 Status: {result['status']}")
                print(f"🔧 Capabilities: {result['capabilities']}")
                print(f"⏱️ Uptime: {result['uptime']:.3f}s")
                print(f"⚡ Performance Score: {result['performance_score']}/10")
                print()
                
                # Show capabilities
                capabilities = self.system.get_capabilities()
                print("🎯 CORE CAPABILITIES:")
                for name, cap in capabilities['core_capabilities'].items():
                    status = "✅" if cap['enabled'] else "❌"
                    print(f"  {status} {name}: {cap['description']}")
                print()
                
                print("🧠 KNOWLEDGE BASES:")
                for name, kb in capabilities['knowledge_bases'].items():
                    print(f"  📚 {name}: {kb['description']}")
                print()
                
                print("🔍 RAG SYSTEMS:")
                for name, rag in capabilities['rag_systems'].items():
                    print(f"  🔍 {name}: {rag['description']}")
                print()
                
                print("🤖 AGI SYSTEMS:")
                for name, agi in capabilities['agi_systems'].items():
                    print(f"  🧠 {name}: {agi['description']}")
                print()
                
                print("📖 LEARNING SYSTEMS:")
                for name, learn in capabilities['learning_systems'].items():
                    print(f"  📖 {name}: {learn['description']}")
                print()
                
                print("✅ VERIFICATION SYSTEMS:")
                for name, verify in capabilities['verification_systems'].items():
                    print(f"  ✅ {name}: {verify['description']}")
                print()
                
                print("🔒 SECURITY SYSTEMS:")
                for name, security in capabilities['security_systems'].items():
                    print(f"  🔒 {name}: {security['description']}")
                print()
                
                print("⚡ OPTIMIZATION SYSTEMS:")
                for name, opt in capabilities['optimization_systems'].items():
                    print(f"  ⚡ {name}: {opt['description']}")
                print()
                
                print("🔄 ADAPTATION SYSTEMS:")
                for name, adapt in capabilities['adaptation_systems'].items():
                    print(f"  🔄 {name}: {adapt['description']}")
                print()
                
                print("🔗 INTEGRATION SYSTEMS:")
                for name, integrate in capabilities['integration_systems'].items():
                    print(f"  🔗 {name}: {integrate['description']}")
                print()
                
                # Test query
                print("🧪 TESTING SYSTEM...")
                test_result = await self.system.query(
                    "System ready for ultimate operations",
                    "i think we need a bigger boat"
                )
                
                if test_result["success"]:
                    print("✅ Test Query Successful!")
                    print(f"📝 Response: {test_result['answer']}")
                    print(f"⏱️ Response Time: {test_result['response_time']:.6f}s")
                    print(f"🔧 Capabilities Used: {len(test_result['capabilities_used'])}")
                else:
                    print(f"❌ Test Query Failed: {test_result.get('error', 'Unknown error')}")
                
                print()
                print("🌊 ULTIMATE DEEPBLUE SELF IS READY!")
                print("🚢 We found a bigger boat and built the ultimate system!")
                print("=" * 60)
                
                return True
            else:
                print(f"❌ FAILED TO START: {result.get('error', 'Unknown error')}")
                return False
                
        except Exception as e:
            logger.error("❌ Startup failed", error=str(e))
            print(f"❌ STARTUP FAILED: {e}")
            return False
    
    async def run_interactive(self):
        """Run interactive mode."""
        if not self.is_running:
            print("❌ System not running. Start the system first.")
            return
        
        print("\n🌊 INTERACTIVE MODE")
        print("=" * 40)
        print("Type 'quit' to exit, 'status' for system status")
        print("Use hack phrase 'i think we need a bigger boat' for full activation")
        print("=" * 40)
        
        while self.is_running:
            try:
                user_input = input("\n🌊 DeepBlue Self> ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                elif user_input.lower() == 'status':
                    status = self.system.get_system_status()
                    print(f"📊 System Status: {status['status']}")
                    print(f"⏱️ Uptime: {status['uptime']:.2f}s")
                    print(f"📈 Queries: {status['metrics']['queries_processed']}")
                    print(f"⚡ Performance: {status['metrics']['performance_score']:.1f}/10")
                elif user_input:
                    result = await self.system.query(user_input)
                    if result["success"]:
                        print(f"🤖 {result['answer']}")
                    else:
                        print(f"❌ Error: {result.get('error', 'Unknown error')}")
                        
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    def stop(self):
        """Stop the system."""
        self.is_running = False
        print("🛑 Ultimate DeepBlue Self stopped.")

def signal_handler(signum, frame):
    """Handle shutdown signals."""
    print("\n🛑 Shutdown signal received...")
    sys.exit(0)

async def main():
    """Main function."""
    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Create manager
    manager = UltimateSelfManager()
    
    # Start system
    success = await manager.start()
    
    if success:
        # Run interactive mode
        await manager.run_interactive()
    
    # Stop system
    manager.stop()

if __name__ == "__main__":
    asyncio.run(main())
