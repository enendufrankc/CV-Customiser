export interface Contact {
  email: string;
  phone: string;
  github?: string;
  linkedin?: string;
}

export interface TechnicalSkills {
  skills: {
    [key: string]: string[];
  };
}

export interface Experience {
  position: string;
  company: string;
  location: string;
  start_date: string;
  end_date?: string;
  responsibilities: string[];
}

export interface Education {
  degree: string;
  institution: string;
  start_date: string;
  end_date: string;
  modules?: string[];
}

export interface PersonalProjects {
  description: string;
}

export interface SoftSkills {
  skills: string[];
}

export interface ResumeData {
  name: string;
  title: string;
  contact: Contact;
  summary: string;
  technical_skills: TechnicalSkills;
  experience: Experience[];
  education: Education[];
  personal_projects: PersonalProjects;
  soft_skills: SoftSkills;
}