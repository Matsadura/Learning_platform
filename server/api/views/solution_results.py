"""Handle solution results related routes."""
from api.views import app_views
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from models import storage
from models.solution_result import Solution_Result
from models.submission import Submission


@app_views.route('/submissions/<submission_id>/results', methods=['GET'])
@jwt_required()
def get_solution_results(submission_id):
    """Retrieves the solution results for a submission."""
    submission = storage.get(Submission, submission_id)
    if not submission:
        return jsonify({'error': 'Submission not found'}), 404
    solution_result = storage.get_specific(Solution_Result,
                                           'submission_id',
                                           submission_id)
    if not solution_result:
        return jsonify({'error': 'Solution result not found'}), 404
    return jsonify(solution_result.to_dict())