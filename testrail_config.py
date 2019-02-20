import testrail


TESTRAIL_URL = 'https://cvcube.testrail.io/'
TESTRAIL_USER = 'v.mytrofanov@mobilunity.com'
TESTRAIL_PASSWORD = 'JXqEwqwtDDuyDsvxVUYc'


class TestRailHelper:

    def __init__(self, run_id=1):
        self.run_id = run_id

    def get_testrail_client(self):
        # Get the TestRail Url
        testrail_url = TESTRAIL_URL
        client = testrail.APIClient(testrail_url)
        # Get and set the TestRail User and Password
        client.user = TESTRAIL_USER
        client.password = TESTRAIL_PASSWORD

        return client

    def update_testrail(self, case_id, result_flag, msg=""):
        "Update TestRail for a given run_id and case_id"
        update_flag = False
        # Get the TestRail client account details
        client = self.get_testrail_client()
        # Update the result in TestRail using send_post function.
        # Parameters for add_result_for_case is the combination of runid and case id.
        # status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed

        if self.run_id is not None:
            try:
                result = client.send_post(
                    'add_result_for_case/%s/%s' % (self.run_id, case_id),
                    {'status_id': result_flag, 'comment': msg})
            except Exception as e:
                print(e)
            else:
                print('Updated test result for case: %s in test run: %s with msg:%s' % (case_id, self.run_id, msg))

        return update_flag

    def get_project_id(self, project_name):
        "Get the project ID using project name"
        client = self.get_testrail_client()
        project_id = None
        projects = client.send_get('get_projects')
        for project in projects:
            if project['name'] == project_name:
                project_id = project['id']
                # project_found_flag=True
                break
        return project_id

    def get_run_id(self, test_run_name, project_name):
        "Get the run ID using test name and project name"
        run_id = None
        client = self.get_testrail_client()
        project_id = self.get_project_id(project_name)
        try:
            test_runs = client.send_get('get_runs/%s' % (project_id))
        except Exception as e:
            print (e)
            return None
        else:
            for test_run in test_runs:
                if test_run['name'] == test_run_name:
                    run_id = test_run['id']
                    break
            return run_id
