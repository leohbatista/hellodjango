import datetime
from typing import Any, Dict
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['my_statement'] = f'This message is dynamically set at {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        return context

