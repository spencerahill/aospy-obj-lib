"""obj_from_name: Get aospy objects given their name string"""
import aospy
from aospy_user import projs, regions, variables


def to_iterable(obj):
    """Return the object if already iterable, otherwise return it as a list."""
    try:
        zip([], obj)
    except TypeError:
        return [obj]
    else:
        return obj


def to_proj(proj):
    """Convert string of an aospy.Proj name to an aospy.Proj instance."""
    orig_type = type(proj)
    if isinstance(proj, aospy.proj.Proj):
        return proj

    elif isinstance(proj, str):
        try:
            return getattr(projs, proj)
        except AttributeError:
            raise AttributeError('Not a recognized Proj name: %s' % proj)

    elif isinstance(proj, (list, tuple)):
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

    if isinstance(model, aospy.model.Model):
        # model.proj = proj
        return model

    elif isinstance(model, str):
        if model in ('all', ['all']):
            model = proj.models.values()
        elif model in ('default', ['default']):
            model = proj.default_models.values()
        else:
            model = proj.models[model]
        # model.proj = proj
        return model

    elif isinstance(model, (list, tuple)):
        model = [to_model(mod, pr) for (mod, pr)
                 in zip(model, to_iterable(proj))]
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

    if isinstance(run, aospy.run.Run):
        return run
        # run.model = model
        # run.proj = proj

    elif isinstance(run, str):
        if run in ('default', ['default']):
            return model.default_runs.keys()
        else:
            run = model.runs[run]
            # run.model = model
            # run.proj = proj
            return run

    elif isinstance(run, (list, tuple)):
        run = [to_run(rn, mod, pr) for (rn, mod, pr)
               in zip(run, to_iterable(model), to_iterable(proj))]
        if orig_type is tuple:
            run = tuple(run)
        return run

    else:
        raise TypeError


def to_var(var):
    """Convert string of an aospy.var name to an aospy.var instance."""
    if isinstance(var, aospy.var.Var):
        return var

    elif isinstance(var, str):
        try:
            var = getattr(variables, var)
        except AttributeError:
            raise AttributeError('Not a recognized Var name: %s' % var)
        return var

    elif isinstance(var, (list, tuple)):
        var_out = [to_var(v) for v in var]
        if isinstance(var, tuple):
            var_out = tuple(var_out)
        return var_out

    else:
        raise TypeError


def to_region(region, proj=False):
    """Convert string of an aospy.Region name to an aospy.Region instance."""
    print region, proj
    if isinstance(region, aospy.region.Region):
        return region

    elif isinstance(region, str):
        if proj and (region in ('all', ['all'])):
            return proj.regions
        else:
            return getattr(regions, region)

    elif isinstance(region, (list, tuple)):
        region_out = [to_region(r, proj=proj) for r in region]
        if isinstance(region, tuple):
            region_out = tuple(region_out)
        return region

    else:
        raise TypeError
