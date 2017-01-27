# from problems.models import Problem
# from submissions.models import Submission
# from utils.models import CodeLang


# def Submit(user, problem, language, code):
#     try:
#         problem = Problem.objects.get(id=problem_id)
#         language = CodeLang.objects.get(pk=language)
#     except Exception as e:
#         return Response(data={'result': 'error', 'detail': str(e)})

#     submission = Submission.objects.create(author=user,
#                                            language=language,
#                                            source_code=code,
#                                            problem=problem)
#     try:
#         print('=' * 20, 'Judge', '=' * 20)
#     except Exception as e:
#         return Response(data={'result': 'error', 'detail': str(e)})
#     return Response(data={'result': 'success', 'submission_id': submission.id})
