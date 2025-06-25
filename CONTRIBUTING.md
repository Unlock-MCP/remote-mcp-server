# Contributing to Remote MCP Server

Thank you for your interest in contributing to the Remote MCP Server project! This guide will help you get started.

## Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/remote-mcp-server.git
   cd remote-mcp-server
   ```

2. **Set up Environment**
   ```bash
   uv venv
   source .venv/bin/activate
   uv add "mcp[cli]" fastapi uvicorn psycopg2-binary python-dotenv
   ```

3. **Configure Database**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

4. **Test Your Setup**
   ```bash
   uvicorn server:app --reload
   npx @modelcontextprotocol/inspector http://localhost:8000/mcp
   ```

## Making Changes

### Code Style
- Follow PEP 8 for Python code
- Use type hints where appropriate
- Add docstrings for new functions
- Keep functions focused and single-purpose

### Testing
- Test your changes with the MCP Inspector
- Verify database connections work
- Check that error handling works properly
- Test with different SQL queries

### Security
- Never commit database credentials
- Ensure all database queries are parameterized
- Validate all user inputs
- Follow principle of least privilege

## Types of Contributions

### Bug Fixes
- Check existing issues before creating new ones
- Include reproduction steps
- Test your fix thoroughly

### Features
- Discuss major changes in an issue first
- Keep changes focused and atomic
- Update documentation as needed

### Documentation
- Fix typos and unclear explanations
- Add examples and use cases
- Update setup instructions

### Examples
- Add useful SQL query examples
- Create deployment guides for new platforms
- Share integration patterns

## Pull Request Process

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Write clean, documented code
   - Test thoroughly
   - Update relevant documentation

3. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

4. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a pull request on GitHub.

## Commit Message Format

Use conventional commits:
- `feat:` new features
- `fix:` bug fixes
- `docs:` documentation changes
- `style:` formatting changes
- `refactor:` code restructuring
- `test:` adding tests
- `chore:` maintenance tasks

## Questions?

- Open an issue for bugs or feature requests
- Check existing issues and discussions
- Review the main tutorial at [UnlockMCP.com](https://unlockmcp.com/guides/how-to-build-a-remote-mcp-server)

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and contribute
- Follow the golden rule