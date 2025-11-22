"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Ticket schema for Santa experience access
class Ticket(BaseModel):
    """
    Tickets for real-world access to Santa’s house experience
    Collection name: "ticket"
    """
    purchaser_name: str = Field(..., min_length=2, description="Name of the purchaser")
    purchaser_email: EmailStr = Field(..., description="Contact email")
    package: str = Field(..., description="Selected package tier, e.g., Standard, VIP, Family")
    quantity: int = Field(1, ge=1, le=10, description="Number of tickets")
    notes: Optional[str] = Field(None, max_length=500, description="Optional message or special requests")
