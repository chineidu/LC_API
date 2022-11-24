from typing import Any, List, Optional

from pydantic import BaseModel
from classification_model.processing.validate import LendingDataSchema


class PredictionResults(BaseModel):
    default_probability: Optional[List[float]]
    default_status: Optional[List[str]]
    model_version: str
    errors: Optional[Any]


class MultipleLendingDataInputs(BaseModel):
    inputs: List[LendingDataSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "acc_now_delinq": 0,
                        "all_util": 54.0,
                        "annual_inc": 80000.0,
                        "collections_12_mths_ex_med": 0,
                        "delinq_2yrs": 0,
                        "dti": 10.58,
                        "il_util": 68.0,
                        "inq_fi": 2.0,
                        "inq_last_12m": 2.0,
                        "inq_last_6mths": 0.0,
                        "int_rate": 7.24,
                        "last_pymnt_amnt": 185.93,
                        "loan_amnt": 6000,
                        "max_bal_bc": 1467.0,
                        "mths_since_last_delinq": 44.0,
                        "mths_since_last_major_derog": 44.0,
                        "mths_since_rcnt_il": 12.0,
                        "open_acc": 7,
                        "open_acc_6m": 0.0,
                        "open_il_12m": 1.0,
                        "open_il_24m": 2.0,
                        "open_rv_12m": 1.0,
                        "out_prncp": 4302.37,
                        "pub_rec": 0,
                        "recoveries": 0.0,
                        "revol_bal": 1975.0,
                        "revol_util": 22.4,
                        "tot_coll_amt": 0.0,
                        "tot_cur_bal": 194559.0,
                        "total_acc": 20,
                        "total_bal_il": 13198.0,
                        "total_cu_tl": 4.0,
                        "total_pymnt": 2042.82,
                        "total_rec_int": 345.19,
                        "total_rec_late_fee": 0.0,
                        "total_rev_hi_lim": 8800.0,
                        "addr_state": "MI",
                        "application_type": "Individual",
                        "emp_length": "10+ years",
                        "grade": "A",
                        "home_ownership": "MORTGAGE",
                        "initial_list_status": "w",
                        "purpose": "vacation",
                        "term": "36 months",
                        "verification_status": "Not Verified",
                        "zip_code": "488xx",
                    }
                ]
            }
        }
