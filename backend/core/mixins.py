class AuditableOwnershipMixin:
    def _set_ownership(self, serializer, is_edit: bool = False):
        current_user = self.request.user
        if is_edit:
            serializer.save(lastmodified_by=current_user)
        else:
            serializer.save(created_by=current_user, lastmodified_by=current_user)

    def perform_create(self, serializer):
        self._set_ownership(serializer)

    def perform_update(self, serializer):
        self._set_ownership(serializer, is_edit=True)

    def get_queryset(self):
        qs = super(AuditableOwnershipMixin, self).get_queryset()
        return qs.filter(created_by=self.request.user)
