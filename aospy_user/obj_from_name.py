"""obj_from_name: Get aospy objects given their name string"""
from aospy import Proj, Model, Run, Var, Region
from aospy_user import projs, regions, variables


def to_proj(proj):
    """Convert string of an aospy.Proj name to an aospy.Proj instance."""
    orig_type = type(proj)
    if type(proj) is Proj:
        return proj

    elif type(proj) is str:
        try:
            return getattr(projs, proj)
        except AttributeError:
            raise AttributeError('Not a recognized Proj name: %s' % proj)

    elif type(proj) in (list, tuple):
        proj = [to_proj(pr) for pr in proj]
        if orig_type is list:
            return proj
        else:
            return tuple(proj)

    else:
        raise TypeError


def to_model(model, proj):
    """Convert string of a Model name to a Model instance."""
    orig_type = type(model)
    proj = to_proj(proj)

    if type(model) is Model:
        # model.proj = proj
        return model

    elif type(model) is str:
        if model in ('all', ['all']):
            model = proj.models.values()
        elif model in ('default', ['default']):
            model = proj.default_models.values()
        else:
            model = proj.models[model]
        # model.proj = proj
        return model

    elif type(model) in (list, tuple):
        model = [to_model(mod, pr) for (mod, pr)
                 in zip(model, proj)]
        if orig_type is tuple:
            model = tuple(model)
        return model

    else:
        raise TypeError


def to_run(run, model, proj):
    """Convert string matching an aospy.run name to an aospy.run instance."""
    orig_type = type(run)
    proj = to_proj(proj)
    model = to_model(model, proj)

    if type(run) is Run:
        return run
        # run.model = model
        # run.proj = proj

    elif type(run) is str:
        if run in ('default', ['default']):
            return model.default_runs.keys()
        else:
            run = model.runs[run]
            # run.model = model
            # run.proj = proj
            return run

    elif type(run) in (list, tuple):
        run = [to_run(rn, mod, pr) for (rn, mod, pr)
               in zip(run, model, proj)]
        if orig_type is tuple:
            run = tuple(run)
        return run

    else:
        raise TypeError


def to_var(var):
    """Convert string of an aospy.var name to an aospy.var instance."""
    if type(var) is Var:
        return var
    elif type(var) is str:
        try:
            var = getattr(variables, var)
        except AttributeError:
            raise AttributeError('Not a recognized Var name: %s' % var)
    elif type(var) in (list, tuple):
        var_out = [to_var(v) for v in var]
        if type(var) is tuple:
            var_out = tuple(var_out)

    return var_out


def to_region(region, proj=False):
    """Convert string of an aospy.Region name to an aospy.Region instance."""
    if type(region) is Region:
        return region
    elif type(region) is str:
        if proj and region in ('all', ['all']):
            region = proj.regions
        else:
            return getattr(regions, region)
    else:
        return region
