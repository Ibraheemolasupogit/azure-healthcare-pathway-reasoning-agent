"""Load and validate simulated healthcare pathway cases."""

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "case_id",
    "pathway_type",
    "referral_date",
    "days_waiting",
    "target_days",
    "current_stage",
    "last_contact_days",
    "diagnostic_status",
    "treatment_status",
    "risk_flags",
    "capacity_issue",
    "admin_blocker",
    "clinical_priority",
    "next_appointment_date",
    "notes",
]


DEFAULT_CASES_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "sample"
    / "simulated_pathway_cases.csv"
)


def validate_required_columns(dataframe: pd.DataFrame) -> None:
    """Validate that the dataset contains every required column."""
    missing_columns = [
        column for column in REQUIRED_COLUMNS if column not in dataframe.columns
    ]

    if missing_columns:
        missing = ", ".join(missing_columns)
        raise ValueError(f"Missing required column(s): {missing}")


def validate_unique_case_ids(dataframe: pd.DataFrame) -> None:
    """Validate that each simulated case has a unique case_id."""
    duplicated_case_ids = sorted(
        dataframe.loc[dataframe["case_id"].duplicated(), "case_id"].unique()
    )

    if duplicated_case_ids:
        duplicates = ", ".join(duplicated_case_ids)
        raise ValueError(f"Duplicate case_id value(s): {duplicates}")


def load_cases(csv_path: str | Path = DEFAULT_CASES_PATH) -> pd.DataFrame:
    """Load simulated pathway cases from CSV and run basic validation."""
    dataframe = pd.read_csv(csv_path)

    validate_required_columns(dataframe)
    validate_unique_case_ids(dataframe)

    return dataframe
