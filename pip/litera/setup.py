from setuptools import setup, find_packages

setup(
    name="litera",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # список зависимостей, например "requests", "pydantic"
    ],
    author="Ваше имя",
    author_email="ваш.email@example.com",
    description="Описание вашего пакета",
    #url="https://github.com/your-repo/my_common_lib",  # если есть
    classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
