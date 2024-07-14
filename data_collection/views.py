from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect
from django.db import transaction, IntegrityError, DatabaseError
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib import messages
import logging
from .forms import WorkerForm, OfficialInformationForm, InstitutionForm, LeaveForm, TransformationForm, PostingTransferForm, UnionForm

logger = logging.getLogger(__name__)

@method_decorator(csrf_protect, name='dispatch')
class MultiStepFormView(View):
    template_name = 'multi_step_form.html'
    
    def get(self, request, *args, **kwargs):
        logger.debug('Rendering the multi-step form.')
        context = {
            'worker_form': WorkerForm(),
            'official_information_form': OfficialInformationForm(),
            'institution_form': InstitutionForm(),
            'leave_form': LeaveForm(),
            'transformation_form': TransformationForm(),
            'posting_transfer_form': PostingTransferForm(),
            'union_form': UnionForm(),
        }
        
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        worker_form = WorkerForm(request.POST)
        official_information_form = OfficialInformationForm(request.POST)
        institution_form = InstitutionForm(request.POST)
        leave_form = LeaveForm(request.POST)
        transformation_form = TransformationForm(request.POST)
        posting_transfer_form = PostingTransferForm(request.POST)
        union_form = UnionForm(request.POST)

        forms = [
            worker_form, official_information_form, institution_form,
            leave_form, transformation_form, posting_transfer_form, union_form
        ]

        try:
            with transaction.atomic():
                if all(form.is_valid() for form in forms):
                    logger.debug('All forms are valid. Proceeding with saving data.')
                    worker = worker_form.save()

                    official_information = official_information_form.save(commit=False)
                    official_information.worker = worker
                    official_information.save()

                    institution = institution_form.save(commit=False)
                    institution.worker = worker
                    institution.save()

                    leave = leave_form.save(commit=False)
                    leave.worker = worker
                    leave.save()

                    transformation = transformation_form.save(commit=False)
                    transformation.worker = worker
                    transformation.save()

                    posting_transfer = posting_transfer_form.save(commit=False)
                    posting_transfer.worker = worker
                    posting_transfer.save()

                    union = union_form.save(commit=False)
                    union.save()
                    union.workers.add(worker)

                    logger.debug('Forms successfully submitted and data saved.')
                    messages.success(request, "Forms successfully submitted!")
                    return redirect('success_url')
                else:
                    messages.error(request, "Please correct the errors in the forms.")
        except IntegrityError as e:
            logger.error(f"Integrity error while saving forms: {e}")
            messages.error(request, "A data integrity error occurred. Please try again.")
        except DatabaseError as e:
            logger.error(f"Database error while saving forms: {e}")
            messages.error(request, "A database error occurred. Please try again.")
        except ValidationError as e:
            logger.error(f"Validation error while saving forms: {e}")
            messages.error(request, "Validation error occurred. Please check the form data and try again.")
        except Exception as e:
            logger.error(f"Error saving forms: {e}")
            messages.error(request, "An error occurred while processing your request. Please try again.")

        context = {
            'worker_form': worker_form,
            'official_information_form': official_information_form,
            'institution_form': institution_form,
            'leave_form': leave_form,
            'transformation_form': transformation_form,
            'posting_transfer_form': posting_transfer_form,
            'union_form': union_form,
        }

        return render(request, self.template_name, context)
