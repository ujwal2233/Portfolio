from django.core.management.base import BaseCommand
from main.models import Profile, Experience, Skill, Project, Certification, Education
from datetime import date

class Command(BaseCommand):
    help = 'Populate portfolio website with complete resume and project data'

    def handle(self, *args, **options):
        # =====================
        # CLEAR EXISTING DATA
        # =====================
        Profile.objects.all().delete()
        Experience.objects.all().delete()
        Skill.objects.all().delete()
        Project.objects.all().delete()
        Certification.objects.all().delete()
        Education.objects.all().delete()

        # =====================
        # PROFILE
        # =====================
        Profile.objects.create(
            name='Ujwal Rajendra Patil',
            title='Software Engineer | Full Stack | AI & ML',
            bio=(
                'Results-driven Software Engineer experienced in building full-stack and AI-powered '
                'applications. Strong foundation in Java, Python, React, Django, and Spring Boot. '
                'Focused on developing scalable, production-ready systems with clean architecture.'
            ),
            email='ujwalpatil2233@gmail.com',
            phone='+91 9022439699',
            location='Dhule, Maharashtra, India',
            github_url='https://github.com/ujwal2233',
            linkedin_url='https://www.linkedin.com/in/ujwalpatil2233/'
        )

        # =====================
        # EXPERIENCE
        # =====================
        Experience.objects.bulk_create([
            Experience(
                title='Software Developer Intern',
                company='Synesius Care Pvt. Ltd.',
                location='Remote',
                start_date=date(2025, 8, 1),
                end_date=date(2025, 12, 31),
                description=(
                    'Worked on hospital management platform using React.js and Next.js. '
                    'Optimized frontend modules and automated data integration workflows '
                    'using Python and SQL while collaborating in Agile sprints.'
                )
            ),

            Experience(
                title='Software Development Intern',
                company='Sumago Infotech',
                location='Nashik, Maharashtra',
                start_date=date(2024, 6, 1),
                end_date=date(2024, 8, 31),
                description=(
                    'Contributed to web application development using Python and Django. '
                    'Implemented backend features, worked on database integration, and '
                    'followed industry-standard development practices under senior mentorship.'
                )
            ),

            Experience(
                title='Artificial Intelligence Intern',
                company='TechSaksham (Microsoft & SAP Initiative)',
                location='Remote',
                start_date=date(2025, 5, 1),
                end_date=date(2025, 6, 30),
                description=(
                    'Developed an AI-powered health assistant chatbot for symptom analysis. '
                    'Improved preprocessing pipelines to reduce data transformation time.'
                )
            ),

            Experience(
                title='Full Stack Developer Intern',
                company='Alhansat Solution',
                location='Remote',
                start_date=date(2024, 10, 1),
                end_date=date(2024, 11, 30),
                description=(
                    'Designed RESTful APIs and full-stack components using React.js and Django. '
                    'Optimized SQL queries and improved overall application performance.'
                )
            ),
        ])

        # =====================
        # SKILLS (CLEAN & REAL)
        # =====================
        skills = [
            # Programming Languages
            ('Core Java', 'language'),
            ('Python', 'language'),
            ('SQL', 'language'),
            ('JavaScript', 'language'),
            ('HTML5', 'language'),
            ('CSS3', 'language'),
            
            # Frameworks
            ('React.js', 'framework'),
            ('Spring Boot', 'framework'),
            ('Django', 'framework'),
            
            # Databases
            ('MySQL', 'database'),
            ('MongoDB', 'database'),
            
            # Data Tools & Concepts
            ('ETL', 'tool'),
            ('Data Modeling', 'concept'),
            ('API-based Data Integration', 'concept'),
            
            # Tools and Technologies
            ('Git-GitHub', 'tool'),
            ('Postman', 'tool'),
            ('Firebase', 'tool'),
            
            # Concepts
            ('REST APIs', 'concept'),
            ('Agile Development', 'concept'),
            ('MVC Architecture', 'concept'),
        ]

        Skill.objects.bulk_create([
            Skill(name=name, category=category, proficiency=85)
            for name, category in skills
        ])

        # =====================
        # PROJECTS (ALL)
        # =====================
        Project.objects.bulk_create([

            Project(
                title='Secure Journal Management System',
                short_description='Role-based secure journal system.',
                description='Implemented authentication and authorization using Spring Security with clean layered architecture.',
                technologies='Java, Spring Boot, Spring Security, MongoDB',
                date_completed=date(2025, 8, 1)
            ),

            Project(
                title='Complaint Classification and Routing System',
                short_description='NLP-based complaint routing system.',
                description='Developed NLP models and a Streamlit dashboard for automated complaint classification.',
                technologies='Python, NLP, Streamlit, MongoDB',
                date_completed=date(2024, 5, 1)
            ),

            Project(
                title='CNN-Based Pneumonia Detection System',
                short_description='Deep learning system for pneumonia detection.',
                description='Built and trained a CNN model on chest X-ray images for pneumonia classification.',
                technologies='Python, CNN, TensorFlow, OpenCV',
                date_completed=date(2024, 4, 1)
            ),

            Project(
                title='Solar Panel Cleaning Alert System',
                short_description='ML-based solar panel cleaning alert system.',
                description='Used sensor data and ML techniques to determine optimal cleaning time for solar panels.',
                technologies='Python, Machine Learning, Arduino',
                date_completed=date(2025, 3, 1)
            ),

            Project(
                title='JalSetu – Water Supply Management System',
                short_description='Digital water supply management platform.',
                description='Built a system to manage assets, billing, and inventory for rural water supply schemes.',
                technologies='React Native, Node.js, MongoDB',
                date_completed=date(2025, 4, 1)
            ),

            Project(
                title='Hospital Management System',
                short_description='Hospital operations management system.',
                description='Developed backend APIs and frontend modules for hospital workflows.',
                technologies='React.js, Django, SQL',
                date_completed=date(2024, 11, 1)
            ),

            Project(
                title='College Timetable Scheduler',
                short_description='Automated college timetable scheduling system.',
                description='Designed a clash-free timetable system with faculty and lecture management.',
                technologies='Java, Android, SQLite',
                date_completed=date(2024, 10, 1)
            ),

            Project(
                title='UJTweet',
                short_description='Microblogging platform.',
                description='Django-based platform with authentication, tweets, media uploads, and search.',
                technologies='Django, Python, Bootstrap',
                date_completed=date(2024, 6, 1)
            ),

            Project(
                title='Music Control System',
                short_description='Web-based music control system.',
                description='Built a Django-based interface to control music playback actions.',
                technologies='Django, Python, JavaScript',
                date_completed=date(2024, 7, 1)
            ),

            Project(
                title='Swashikahsrthi',
                short_description='Custom domain-specific software system.',
                description='Developed a modular backend-driven application tailored to specific requirements.',
                technologies='Python, Django',
                date_completed=date(2024, 8, 1)
            ),

            Project(
                title='Tic Tac Toe',
                short_description='Classic Tic Tac Toe game.',
                description='Implemented game logic and UI interactions.',
                technologies='JavaScript, HTML, CSS',
                date_completed=date(2023, 6, 1)
            ),

            Project(
                title='Rock Paper Scissors',
                short_description='Interactive game.',
                description='Built a simple browser-based game to practice logic and events.',
                technologies='JavaScript, HTML, CSS',
                date_completed=date(2023, 5, 1)
            ),
        ])

        # =====================
        # CERTIFICATIONS
        # =====================
        Certification.objects.bulk_create([
            Certification(
                title='Programming in Java',
                issuer='NPTEL',
                issue_date=date(2024, 6, 1),
                credential_url='https://nptel.ac.in/'
            ),
            Certification(
                title='German I',
                issuer='NPTEL',
                issue_date=date(2025, 1, 1),
                credential_url='https://nptel.ac.in/'
            ),
            Certification(
                title='Full Stack Web Development',
                issuer='Udemy',
                issue_date=date(2024, 3, 1),
                credential_url='https://udemy.com/'
            ),
            Certification(
                title='Python Foundation',
                issuer='Infosys Springboard',
                issue_date=date(2022, 8, 1),
                credential_url='https://infosys.com/springboard'
            ),
            Certification(
                title='Young Professional',
                issuer='TCS iON',
                issue_date=date(2023, 5, 1),
                credential_url='https://www.tcsion.com/'
            ),
            Certification(
                title='Programming in C',
                issuer='Spoken Tutorial',
                issue_date=date(2023, 9, 1),
                credential_url='https://spoken-tutorial.org/'
            ),
            Certification(
                title='Programming in C++',
                issuer='Spoken Tutorial',
                issue_date=date(2023, 10, 1),
                credential_url='https://spoken-tutorial.org/'
            ),
        ])

        # =====================
        # EDUCATION
        # =====================
        Education.objects.bulk_create([
            Education(
                degree='Bachelor of Technology',
                institution='SVKM\'s Institute of Technology',
                field_of_study='Computer Engineering',
                start_date=date(2022, 11, 1),
                end_date=date(2026, 6, 30),
                gpa='7.75 CGPA',
                description='Dhule, Maharashtra'
            ),
            Education(
                degree='HSC (Higher Secondary Certificate)',
                institution='Jai Hind Junior College',
                field_of_study='Science',
                start_date=date(2020, 6, 1),
                end_date=date(2022, 5, 31),
                gpa='78.20%',
                description='Dhule, Maharashtra'
            ),
            Education(
                degree='SSC (Secondary School Certificate)',
                institution='Jai Hind High School',
                field_of_study='General',
                start_date=date(2019, 6, 1),
                end_date=date(2020, 5, 31),
                gpa='90.00%',
                description='Dhule, Maharashtra'
            ),
        ])

        self.stdout.write(self.style.SUCCESS('✅ Portfolio database populated successfully'))
