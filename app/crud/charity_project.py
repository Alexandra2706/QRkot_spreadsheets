from typing import List, Optional

from sqlalchemy import select

from app.core.db import AsyncSession
from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> List[CharityProject]:
        projects_list = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == 1
            )
        )
        projects_list = projects_list.scalars().all()
        projects_list = sorted(
            projects_list,
            key=lambda project: project.close_date - project.create_date
            )
        return projects_list


charity_project_crud = CRUDCharityProject(CharityProject)
