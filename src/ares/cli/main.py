"""Minimal ARES CLI entrypoint.

Only foundational commands exist today. Domain commands are added from Phase 4 onward,
once the orchestrator and governance layers are in place.
"""

from __future__ import annotations

import typer

from ares import __version__

app = typer.Typer(
    help="ARES Enterprise — command-line interface.",
    no_args_is_help=True,
    add_completion=False,
)


@app.command()
def version() -> None:
    """Print the ARES version."""

    typer.echo(__version__)


@app.command()
def info() -> None:
    """Show basic platform and configuration information."""

    from ares.core.config import Settings

    settings = Settings()
    typer.echo(f"ARES Enterprise {__version__}")
    typer.echo(f"environment: {settings.environment}")
    typer.echo(f"default profile: {settings.default_profile.value}")
    typer.echo(f"approval required: {settings.require_approval}")


if __name__ == "__main__":
    app()
