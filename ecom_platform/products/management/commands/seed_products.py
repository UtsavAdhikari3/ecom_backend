from django.core.management.base import BaseCommand
from products.models import Product
import random

class Command(BaseCommand):
    help = "Seed products into database"

    def handle(self, *args, **kwargs):
        products = [
            {"name": "iPhone 15", "description": "Latest Apple smartphone", "price": 999.99, "stock": 15},
            {"name": "Samsung Galaxy S24", "description": "Flagship Android phone", "price": 899.99, "stock": 20},
            {"name": "MacBook Pro 14\"", "description": "Apple M3 powerful laptop", "price": 1999.99, "stock": 8},
            {"name": "Dell XPS 13", "description": "Ultra portable laptop", "price": 1299.99, "stock": 10},
            {"name": "Gaming PC", "description": "High performance desktop PC", "price": 2200.00, "stock": 5},
            
            {"name": "Mechanical Keyboard", "description": "RGB backlit keyboard", "price": 149.99, "stock": 30},
            {"name": "Wireless Mouse", "description": "Ergonomic mouse", "price": 49.99, "stock": 50},
            {"name": "Gaming Mouse", "description": "High DPI gaming mouse", "price": 79.99, "stock": 40},
            {"name": "27\" Monitor", "description": "144Hz gaming monitor", "price": 299.99, "stock": 12},
            {"name": "4K Monitor", "description": "Ultra HD display", "price": 499.99, "stock": 10},

            {"name": "AirPods Pro", "description": "Noise cancelling earbuds", "price": 249.99, "stock": 25},
            {"name": "Sony WH-1000XM5", "description": "Premium headphones", "price": 399.99, "stock": 18},
            {"name": "Bluetooth Speaker", "description": "Portable speaker", "price": 99.99, "stock": 35},
            
            {"name": "iPad Air", "description": "Apple tablet", "price": 599.99, "stock": 14},
            {"name": "Samsung Galaxy Tab", "description": "Android tablet", "price": 549.99, "stock": 16},
            
            {"name": "Smart Watch", "description": "Fitness tracking smartwatch", "price": 199.99, "stock": 28},
            {"name": "Apple Watch Series 9", "description": "Advanced smartwatch", "price": 399.99, "stock": 12},
            
            {"name": "External SSD 1TB", "description": "Fast portable storage", "price": 129.99, "stock": 22},
            {"name": "USB-C Hub", "description": "Multiport adapter", "price": 39.99, "stock": 45},
            {"name": "Laptop Stand", "description": "Adjustable stand", "price": 29.99, "stock": 40},

            {"name": "Webcam HD", "description": "1080p webcam", "price": 79.99, "stock": 20},
            {"name": "Microphone", "description": "Studio quality mic", "price": 149.99, "stock": 15},
            {"name": "Ring Light", "description": "Lighting for streaming", "price": 59.99, "stock": 25},

            {"name": "PlayStation 5", "description": "Next-gen console", "price": 499.99, "stock": 7},
            {"name": "Xbox Series X", "description": "Microsoft console", "price": 499.99, "stock": 9},
            {"name": "Nintendo Switch", "description": "Portable gaming console", "price": 299.99, "stock": 13},

            {"name": "Gaming Chair", "description": "Ergonomic chair", "price": 249.99, "stock": 11},
            {"name": "Desk Lamp", "description": "LED adjustable lamp", "price": 34.99, "stock": 30},
            {"name": "Backpack", "description": "Laptop backpack", "price": 69.99, "stock": 27},

            {"name": "Power Bank", "description": "10000mAh portable charger", "price": 39.99, "stock": 50},
            {"name": "Phone Case", "description": "Shockproof case", "price": 19.99, "stock": 60},
        ]

        for p in products:
            Product.objects.create(**p)

        self.stdout.write(self.style.SUCCESS("Products seeded successfully"))