import setuptools

setuptools.setup(
    name="<name>",
    version="0.1.0",
    description="Snake Game with AI",
    license="TODO",
    author="Constantin Gahr",
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[],
    setup_requires=["pytest-runner"],
    test_suite="pytest",
    tests_require=["pytest"],
)
