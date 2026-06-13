from pathlib import Path

import pandas as pd
import pytest

from src.data.load_cases import REQUIRED_COLUMNS, load_cases


def test_load_cases_returns_dataframe_with_expected_columns() -> None:
    dataframe = load_cases()

    assert isinstance(dataframe, pd.DataFrame)
    assert list(dataframe.columns) == REQUIRED_COLUMNS


def test_sample_dataset_contains_30_synthetic_cases() -> None:
    dataframe = load_cases()

    assert len(dataframe) == 30
    assert dataframe["case_id"].str.startswith("SIM-").all()
    assert dataframe["notes"].str.contains("Synthetic case:").all()


def test_load_cases_rejects_missing_required_columns(tmp_path: Path) -> None:
    csv_path = tmp_path / "missing_columns.csv"
    pd.DataFrame({"case_id": ["SIM-9999"]}).to_csv(csv_path, index=False)

    with pytest.raises(ValueError, match="Missing required column"):
        load_cases(csv_path)


def test_load_cases_rejects_duplicate_case_ids(tmp_path: Path) -> None:
    csv_path = tmp_path / "duplicate_case_ids.csv"
    dataframe = pd.DataFrame(
        [
            {
                "case_id": "SIM-9999",
                "pathway_type": "Cancer 2WW",
                "referral_date": "2026-06-01",
                "days_waiting": 12,
                "target_days": 14,
                "current_stage": "Initial booking",
                "last_contact_days": 1,
                "diagnostic_status": "Booked",
                "treatment_status": "Not required",
                "risk_flags": "none",
                "capacity_issue": "No",
                "admin_blocker": "No",
                "clinical_priority": "Routine",
                "next_appointment_date": "2026-06-15",
                "notes": "Synthetic case: duplicate test record.",
            },
            {
                "case_id": "SIM-9999",
                "pathway_type": "Cancer 2WW",
                "referral_date": "2026-06-02",
                "days_waiting": 11,
                "target_days": 14,
                "current_stage": "Initial booking",
                "last_contact_days": 2,
                "diagnostic_status": "Booked",
                "treatment_status": "Not required",
                "risk_flags": "none",
                "capacity_issue": "No",
                "admin_blocker": "No",
                "clinical_priority": "Routine",
                "next_appointment_date": "2026-06-16",
                "notes": "Synthetic case: duplicate test record.",
            },
        ],
        columns=REQUIRED_COLUMNS,
    )
    dataframe.to_csv(csv_path, index=False)

    with pytest.raises(ValueError, match="Duplicate case_id"):
        load_cases(csv_path)
