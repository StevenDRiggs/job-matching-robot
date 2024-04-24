from job_seekers.models import Industry as JSIndustry


class Industry(JSIndustry):
    class Meta:
        verbose_name_plural = 'industries'
