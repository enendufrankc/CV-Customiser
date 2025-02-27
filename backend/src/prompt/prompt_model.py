from typing import List, Optional, Dict, Union
from pydantic import BaseModel, HttpUrl
import json

class ContactInfo(BaseModel):
    email: str
    phone: str
    github: Optional[HttpUrl] = None
    linkedin: Optional[HttpUrl] = None
    portfolio: Optional[HttpUrl] = None
    medium: Optional[HttpUrl] = None

class TechnicalSkills(BaseModel):
    skills: Dict[str, List[str]]  

class Experience(BaseModel):
    company: str
    location: str
    position: str
    start_date: str
    end_date: Optional[str]  
    responsibilities: List[str]

class Education(BaseModel):
    institution: str
    degree: str
    start_date: str
    end_date: str
    modules: Optional[List[str]] = None

class PersonalProjects(BaseModel):
    description: str

class SoftSkills(BaseModel):
    skills: List[str] 

class CV(BaseModel):
    name: str
    title: str
    contact: ContactInfo
    summary: str
    technical_skills: TechnicalSkills
    experience: List[Experience]
    personal_projects: PersonalProjects
    soft_skills: SoftSkills
    education: List[Education]

